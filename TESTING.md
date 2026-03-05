# Testing Strategy for Quick-Calc

## Unit Testing
- Tested each arithmetic operation individually: add, subtract, multiply, divide, and clear.
- Covered edge cases:
  - Negative numbers
  - Decimal numbers
  - Large numbers
  - Division by zero (raises `ValueError`)

## Integration Testing
- Tested full user interaction flow:
  - Enter two numbers and perform addition.
  - Press Clear after a calculation and verify display resets to zero.

## Testing Pyramid
- Most tests are **unit tests** (8 total)
- Fewer **integration tests** (2 total)
- Reflects standard Testing Pyramid: many fast unit tests, few slower integration tests.

## Black-box vs White-box
- **Unit tests:** White-box testing — we know internal implementation.
- **Integration tests:** Black-box testing — simulate user actions without looking inside functions.

## Functional vs Non-Functional
- **Functional tests:** Calculator logic correctness.
- **Non-functional tests:** Not tested (performance, UI).

## Regression Testing
- The test suite can be re-run whenever new features are added to catch regressions.

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_full_addition_flow | Integration | Pass |
| test_clear_resets_calculator | Integration | Pass |
