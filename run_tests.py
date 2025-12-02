#!/usr/bin/env python3
"""
Test runner for all Advent of Code solutions
"""
import sys
import importlib
from pathlib import Path


def run_all_tests():
    """Run tests for all day solutions"""
    solutions_dir = Path(__file__).parent / "solutions"
    test_failed = False

    for day_file in sorted(solutions_dir.glob("day*.py")):
        if day_file.name == "__init__.py":
            continue

        module_name = f"solutions.{day_file.stem}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "test"):
                print(f"\n{'='*50}")
                print(f"Running tests for {module_name}...")
                print(f"{'='*50}")
                module.test()
            else:
                print(f"Skipping {module_name} (no test function found)")
        except Exception as e:
            print(f"Error testing {module_name}: {e}")
            import traceback
            traceback.print_exc()
            test_failed = True

    if test_failed:
        print("\n❌ Some tests failed!")
        sys.exit(1)
    else:
        print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
