#!/bin/bash
# Quick test runner script for PBIXRay tests

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}PBIXRay Test Suite${NC}"
echo -e "${BLUE}==================${NC}\n"

# Check if pytest is installed
if ! python3 -m pytest --version > /dev/null 2>&1; then
    echo -e "${YELLOW}pytest not found. Installing test dependencies...${NC}"
    pip install -r test/requirements.txt
fi

# Parse command line arguments
case "$1" in
    all)
        echo -e "${GREEN}Running all tests...${NC}"
        python3 -m pytest test/ -v
        ;;
    init)
        echo -e "${GREEN}Running initialization tests...${NC}"
        python3 -m pytest test/test_api_initialization.py -v
        ;;
    metadata)
        echo -e "${GREEN}Running metadata tests...${NC}"
        python3 -m pytest test/test_api_metadata.py -v
        ;;
    dax)
        echo -e "${GREEN}Running DAX tests...${NC}"
        python3 -m pytest test/test_api_dax.py -v
        ;;
    relationships)
        echo -e "${GREEN}Running relationships and RLS tests...${NC}"
        python3 -m pytest test/test_api_relationships_rls.py -v
        ;;
    table)
        echo -e "${GREEN}Running get_table tests...${NC}"
        python3 -m pytest test/test_api_get_table.py -v
        ;;
    integration)
        echo -e "${GREEN}Running integration tests...${NC}"
        python3 -m pytest test/test_api_integration.py -v
        ;;
    coverage)
        echo -e "${GREEN}Running tests with coverage report...${NC}"
        python3 -m pytest test/ --cov=pbixray --cov-report=html --cov-report=term
        echo -e "${GREEN}Coverage report generated in htmlcov/index.html${NC}"
        ;;
    validate)
        echo -e "${GREEN}Validating test setup...${NC}"
        python3 test/validate_setup.py
        ;;
    quick)
        echo -e "${GREEN}Running quick test (first file only)...${NC}"
        python3 -m pytest test/test_api_initialization.py::TestInitialization::test_pbix_initialization -v
        ;;
    *)
        echo -e "Usage: $0 {all|init|metadata|dax|relationships|table|integration|coverage|validate|quick}"
        echo -e ""
        echo -e "Test categories:"
        echo -e "  ${GREEN}all${NC}           - Run all tests"
        echo -e "  ${GREEN}init${NC}          - Initialization tests"
        echo -e "  ${GREEN}metadata${NC}      - Metadata properties tests"
        echo -e "  ${GREEN}dax${NC}           - DAX and Power Query tests"
        echo -e "  ${GREEN}relationships${NC} - Relationships and RLS tests"
        echo -e "  ${GREEN}table${NC}         - get_table() method tests"
        echo -e "  ${GREEN}integration${NC}   - Integration tests"
        echo -e "  ${GREEN}coverage${NC}      - Run all tests with coverage report"
        echo -e "  ${GREEN}validate${NC}      - Validate test setup"
        echo -e "  ${GREEN}quick${NC}         - Run a single quick test"
        echo -e ""
        echo -e "Examples:"
        echo -e "  $0 all          # Run all tests"
        echo -e "  $0 coverage     # Run with coverage"
        echo -e "  $0 validate     # Check test setup"
        ;;
esac
