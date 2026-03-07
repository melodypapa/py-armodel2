"""CompuRationalCoeffs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_nominator_denominator import (
    CompuNominatorDenominator,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompuRationalCoeffs(ARObject):
    """AUTOSAR CompuRationalCoeffs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPU-RATIONAL-COEFFS"


    compu_numerator: Optional[CompuNominatorDenominator]
    compu_denominator: Optional[CompuNominatorDenominator]
    _DESERIALIZE_DISPATCH = {
        "COMPU-NUMERATOR": lambda obj, elem: setattr(obj, "compu_numerator", SerializationHelper.deserialize_by_tag(elem, "CompuNominatorDenominator")),
        "COMPU-DENOMINATOR": lambda obj, elem: setattr(obj, "compu_denominator", SerializationHelper.deserialize_by_tag(elem, "CompuNominatorDenominator")),
    }


    def __init__(self) -> None:
        """Initialize CompuRationalCoeffs."""
        super().__init__()
        self.compu_numerator: Optional[CompuNominatorDenominator] = None
        self.compu_denominator: Optional[CompuNominatorDenominator] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuRationalCoeffs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuRationalCoeffs, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_numerator
        if self.compu_numerator is not None:
            serialized = SerializationHelper.serialize_item(self.compu_numerator, "CompuNominatorDenominator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-NUMERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize compu_denominator
        if self.compu_denominator is not None:
            serialized = SerializationHelper.serialize_item(self.compu_denominator, "CompuNominatorDenominator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-DENOMINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuRationalCoeffs":
        """Deserialize XML element to CompuRationalCoeffs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuRationalCoeffs object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuRationalCoeffs, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPU-NUMERATOR":
                setattr(obj, "compu_numerator", SerializationHelper.deserialize_by_tag(child, "CompuNominatorDenominator"))
            elif tag == "COMPU-DENOMINATOR":
                setattr(obj, "compu_denominator", SerializationHelper.deserialize_by_tag(child, "CompuNominatorDenominator"))

        return obj



class CompuRationalCoeffsBuilder(BuilderBase):
    """Builder for CompuRationalCoeffs with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompuRationalCoeffs = CompuRationalCoeffs()


    def with_compu_numerator(self, value: Optional[CompuNominatorDenominator]) -> "CompuRationalCoeffsBuilder":
        """Set compu_numerator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'compu_numerator' is required and cannot be None")
        self._obj.compu_numerator = value
        return self

    def with_compu_denominator(self, value: Optional[CompuNominatorDenominator]) -> "CompuRationalCoeffsBuilder":
        """Set compu_denominator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'compu_denominator' is required and cannot be None")
        self._obj.compu_denominator = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "compuDenominator",
        "compuNumerator",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompuRationalCoeffs:
        """Build and return the CompuRationalCoeffs instance with validation."""
        self._validate_instance()
        return self._obj