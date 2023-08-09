set -e


RAW=$(gh repo list $GITHUB_ACTOR --visibility public --json url)
URLS=$(python $GITHUB_ACTION_PATH/src get-clone-urls $RAW)


echo "::group::DEBUG"
echo "RAW: '$RAW'"
echo "URLS: '$URLS'"
echo "::endgroup::"


## Folder to store all the cloned repositories
mkdir $GITHUB_WORKSPACE/../lineosaurus-workspace
cd $GITHUB_WORKSPACE/../lineosaurus-workspace


echo "::group::Cloning"
for url in $URLS; do
    git clone $url
done
echo "::endgroup::"