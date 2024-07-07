# Impure Python environment based on
# https://github.com/NixOS/nixpkgs/blob/b40f62f3f846723f61d846a0edb14228e1055301/doc/languages-frameworks/python.section.md#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems-how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems

{ pkgs ? import <nixpkgs> { }, ... }:

let
  pythonPackages = pkgs.python312Packages;
in
pkgs.mkShell {
  src = ./.;
  name = "impurePythonEnv";
  venvDir = "./env";
  packages = [ pkgs.gitlint ];
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pythonPackages.python

    # This executes some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    pythonPackages.venvShellHook

    # Those are dependencies that we would like to use from nixpkgs, which will
    # add them to PYTHONPATH and thus make them accessible from within the
    # venv.
    # pythonPackages.sympy
  ];

  # Run this command, only after creating the virtual environment
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -e .[devel]
  '';

  postShellHook = ''
    # Allow pip to install wheels
    unset SOURCE_DATE_EPOCH
    alias mypy="mypy --config-file $src/pyproject.toml"
  '';
}
