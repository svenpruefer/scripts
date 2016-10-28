;; Make a non-standard key binding.  We can put this in
;; c-mode-base-map because c-mode-map, c++-mode-map, and so on,
;; inherit from it.
(defun my-c-initialization-hook ()
  (define-key c-mode-base-map "\C-m" 'c-context-line-break))
(add-hook 'c-initialization-hook 'my-c-initialization-hook)

(require 'package)
(package-initialize)

(add-to-list 'load-path "~/.emacs.d")
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)

(require 'auto-complete)
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/elpa/auto.complete-1.4/dict")
(ac-config-default)
(global-auto-complete-mode t)

(setq-default TeX-master nil) ; Query for master file.

(require 'iso-transl)

(load "auctex.el" nil t t)

;; No idea how this should work: It is supposed to automatically load the auto-complete minor mode when the major mode is active.
;;(require 'LaTeX/PS-mode)
;;(defun turn-on-paredit () (auto-complete-mode 1))

(add-hook 'LaTeX-mode-hook 'my-latex-mode-hook)
(defun my-latex-mode-hook ()
  (auto-complete-mode 1)
  (yas-minor-mode 1)
  (reftex-mode 1))

;; offset customizations not in my-c-style
;; This will take precedence over any setting of the syntactic symbol
;; made by a style.
(setq c-offsets-alist '((member-init-intro . ++)))

;; Create my personal style.
(defconst my-c-style
  '((c-tab-always-indent        . t)
    (c-comment-only-line-offset . 4)
    (c-hanging-braces-alist     . ((substatement-open after)
                                   (brace-list-open)))
    (c-hanging-colons-alist     . ((member-init-intro before)
                                   (inher-intro)
                                   (case-label after)
                                   (label after)
                                   (access-label after)))
    (c-cleanup-list             . (scope-operator
                                   empty-defun-braces
                                   defun-close-semi))
    (c-offsets-alist            . ((arglist-close . c-lineup-arglist)
                                   (substatement-open . 0)
                                   (case-label        . 4)
                                   (block-open        . 0)
                                   (knr-argdecl-intro . -)))
    (c-echo-syntactic-information-p . t))
  "My C Programming Style")
(c-add-style "PERSONAL" my-c-style)

;; Customizations for all modes in CC Mode.
(defun my-c-mode-common-hook ()
  ;; set my personal style for the current buffer
  (c-set-style "PERSONAL")
  ;; other customizations
  (setq tab-width 8
        ;; this will make sure spaces are used instead of tabs
        indent-tabs-mode nil)
  ;; we like auto-newline, but not hungry-delete
  (c-toggle-auto-newline 1))
(add-hook 'c-mode-common-hook 'my-c-mode-common-hook)

; SyncTeX basics

; un-urlify and urlify-escape-only should be improved to handle all special characters, not only spaces.
; The fix for spaces is based on the first comment on http://emacswiki.org/emacs/AUCTeX#toc20

(defun un-urlify (fname-or-url)
  "Transform file:///absolute/path from Gnome into /absolute/path with very limited support for special characters"
  (if (string= (substring fname-or-url 0 8) "file:///")
      (url-unhex-string (substring fname-or-url 7))
    fname-or-url))

(defun urlify-escape-only (path)
  "Handle special characters for urlify"
  (replace-regexp-in-string " " "%20" path))

(defun urlify (absolute-path)
  "Transform /absolute/path to file:///absolute/path for Gnome with very limited support for special characters"
  (if (string= (substring absolute-path 0 1) "/")
      (concat "file://" (urlify-escape-only absolute-path))
      absolute-path))



; SyncTeX backward search - based on http://emacswiki.org/emacs/AUCTeX#toc20, reproduced on http://tex.stackexchange.com/a/49840/21017

(defun th-evince-sync (file linecol &rest ignored)
  (let* ((fname (un-urlify file))
         (buf (find-file fname))
         (line (car linecol))
         (col (cadr linecol)))
    (if (null buf)
        (message "[Synctex]: Could not open %s" fname)
      (switch-to-buffer buf)
      (goto-line (car linecol))
      (unless (= col -1)
        (move-to-column col)))))

(defvar *dbus-evince-signal* nil)

(defun enable-evince-sync ()
  (require 'dbus)
  ; cl is required for setf, taken from: http://lists.gnu.org/archive/html/emacs-orgmode/2009-11/msg01049.html
  (require 'cl)
  (when (and
         (eq window-system 'x)
         (fboundp 'dbus-register-signal))
    (unless *dbus-evince-signal*
      (setf *dbus-evince-signal*
            (dbus-register-signal
             :session nil "/org/gnome/evince/Window/0"
             "org.gnome.evince.Window" "SyncSource"
             'th-evince-sync)))))

(add-hook 'LaTeX-mode-hook 'enable-evince-sync)




; SyncTeX forward search - based on http://tex.stackexchange.com/a/46157

;; universal time, need by evince
(defun utime ()
  (let ((high (nth 0 (current-time)))
        (low (nth 1 (current-time))))
   (+ (* high (lsh 1 16) ) low)))

;; Forward search.
;; Adapted from http://dud.inf.tu-dresden.de/~ben/evince_synctex.tar.gz
(defun auctex-evince-forward-sync (pdffile texfile line)
  (let ((dbus-name
     (dbus-call-method :session
               "org.gnome.evince.Daemon"  ; service
               "/org/gnome/evince/Daemon" ; path
               "org.gnome.evince.Daemon"  ; interface
               "FindDocument"
               (urlify pdffile)
               t     ; Open a new window if the file is not opened.
               )))
    (dbus-call-method :session
          dbus-name
          "/org/gnome/evince/Window/0"
          "org.gnome.evince.Window"
          "SyncView"
          (urlify-escape-only texfile)
          (list :struct :int32 line :int32 1)
  (utime))))

(defun auctex-evince-view ()
  (let ((pdf (file-truename (concat default-directory
                    (TeX-master-file (TeX-output-extension)))))
    (tex (buffer-file-name))
    (line (line-number-at-pos)))
    (auctex-evince-forward-sync pdf tex line)))

;; New view entry: Evince via D-bus.
(setq TeX-view-program-list '())
(add-to-list 'TeX-view-program-list
         '("EvinceDbus" auctex-evince-view))

;; Prepend Evince via D-bus to program selection list
;; overriding other settings for PDF viewing.
(setq TeX-view-program-selection '())
(add-to-list 'TeX-view-program-selection
         '(output-pdf "EvinceDbus"))

(setq TeX-PDF-mode t)
(setq TeX-source-correlate-mode t)
(setq TeX-source-correlate-start-server t)
