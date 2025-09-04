Clear-Host
python -m pip install . --no-build-isolation
python -m nanobind.stubgen -m imui._C -o python/imui/_C.pyi

$imuiLocation = python -c "import imui, os; print(os.path.dirname(imui.__file__))" 2>$null

if (-not $imuiLocation) {
    Write-Host "Error: Unable to locate imui installation directory" -ForegroundColor Red
    exit 1
}

$sourceFile = "python/imui/_C.pyi"
$destination = Join-Path -Path $imuiLocation -ChildPath "_C.pyi"

try {
    Copy-Item -Path $sourceFile -Destination $destination -Force
    Write-Host "Successfully copied stub file to: $destination" -ForegroundColor Green
}
catch {
    Write-Host "Copy failed: $_" -ForegroundColor Red
    exit 1
}