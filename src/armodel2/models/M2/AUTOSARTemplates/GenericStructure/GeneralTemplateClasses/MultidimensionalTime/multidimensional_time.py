"""MultidimensionalTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 164)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_MultidimensionalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultidimensionalTime(ARObject):
    """AUTOSAR MultidimensionalTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MULTIDIMENSIONAL-TIME"


    cse_code: Optional[CseCodeType]
    cse_code_factor: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "CSE-CODE": lambda obj, elem: setattr(obj, "cse_code", SerializationHelper.deserialize_by_tag(elem, "CseCodeType")),
        "CSE-CODE-FACTOR": lambda obj, elem: setattr(obj, "cse_code_factor", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize MultidimensionalTime."""
        super().__init__()
        self.cse_code: Optional[CseCodeType] = None
        self.cse_code_factor: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize MultidimensionalTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultidimensionalTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cse_code
        if self.cse_code is not None:
            serialized = SerializationHelper.serialize_item(self.cse_code, "CseCodeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CSE-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cse_code_factor
        if self.cse_code_factor is not None:
            serialized = SerializationHelper.serialize_item(self.cse_code_factor, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CSE-CODE-FACTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultidimensionalTime":
        """Deserialize XML element to MultidimensionalTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultidimensionalTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultidimensionalTime, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CSE-CODE":
                setattr(obj, "cse_code", SerializationHelper.deserialize_by_tag(child, "CseCodeType"))
            elif tag == "CSE-CODE-FACTOR":
                setattr(obj, "cse_code_factor", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class MultidimensionalTimeBuilder(BuilderBase):
    """Builder for MultidimensionalTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultidimensionalTime = MultidimensionalTime()


    def with_cse_code(self, value: Optional[CseCodeType]) -> "MultidimensionalTimeBuilder":
        """Set cse_code attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cse_code' is required and cannot be None")
        self._obj.cse_code = value
        return self

    def with_cse_code_factor(self, value: Optional[Integer]) -> "MultidimensionalTimeBuilder":
        """Set cse_code_factor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cse_code_factor' is required and cannot be None")
        self._obj.cse_code_factor = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cseCode",
        "cseCodeFactor",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MultidimensionalTime:
        """Build and return the MultidimensionalTime instance with validation."""
        self._validate_instance()
        return self._obj