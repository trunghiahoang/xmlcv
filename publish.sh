#!/bin/bash
# Script to publish XMLCV to PyPI

set -e

echo "🚀 Building XMLCV package..."

# Clean old builds
rm -rf build/ dist/ *.egg-info

# Build package
python -m build

echo "✅ Build complete!"
echo ""
echo "📦 Package files:"
ls -lh dist/

echo ""
echo "🔍 Checking package..."
twine check dist/*

echo ""
echo "📤 Ready to upload!"
echo ""
echo "To upload to TestPyPI:"
echo "  twine upload --repository testpypi dist/*"
echo ""
echo "To upload to PyPI:"
echo "  twine upload dist/*"
echo ""
read -p "Upload to TestPyPI now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    twine upload --repository testpypi dist/*
    echo "✅ Uploaded to TestPyPI!"
fi
