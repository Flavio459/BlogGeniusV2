{pkgs}: {
  deps = [
    pkgs.python310Packages.openai
    pkgs.imagemagick
    pkgs.libyaml
  ];
}
