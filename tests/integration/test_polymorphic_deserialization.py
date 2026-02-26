"""Integration tests for polymorphic deserialization with wrapper elements."""

import pytest
from pathlib import Path
from armodel2.models import AUTOSAR, ConstantSpecification
from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter


class TestPolymorphicDeserialization:
    """Test polymorphic deserialization of wrapper elements."""

    def test_constant_specification_with_numerical_value(self, tmp_path: Path):
        """Test ConstantSpecification with NumericalValueSpecification."""
        arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Test</SHORT-NAME>
      <ELEMENTS>
        <CONSTANT-SPECIFICATION>
          <SHORT-NAME>MyConstant</SHORT-NAME>
          <VALUE-SPEC>
            <NUMERICAL-VALUE-SPECIFICATION>
              <SHORT-LABEL>MyValue</SHORT-LABEL>
              <VALUE>42</VALUE>
            </NUMERICAL-VALUE-SPECIFICATION>
          </VALUE-SPEC>
        </CONSTANT-SPECIFICATION>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

        arxml_file = tmp_path / "test.arxml"
        arxml_file.write_text(arxml_content)

        reader = ARXMLReader()
        autosar = reader.load_arxml(str(arxml_file))

        constant = autosar.ar_packages[0].elements[0]
        assert isinstance(constant, ConstantSpecification)
        assert constant.value_spec is not None
        assert type(constant.value_spec).__name__ == "NumericalValueSpecification"

        # Test round-trip
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter(pretty_print=True)
        writer.save_arxml(str(output_file), autosar)

        output_content = output_file.read_text()
        assert "<NUMERICAL-VALUE-SPECIFICATION>" in output_content
        assert "<SHORT-LABEL>MyValue</SHORT-LABEL>" in output_content
        assert "<VALUE>42</VALUE>" in output_content
