"""ValueList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 350)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 459)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class ValueList(ARObject):
    """AUTOSAR ValueList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VALUE-LIST"


    v: Optional[Numerical]
    _DESERIALIZE_DISPATCH = {
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
    }


    def __init__(self) -> None:
        """Initialize ValueList."""
        super().__init__()
        self.v: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize ValueList to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ValueList, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize v (primitive)
        if self.v is not None:
            child = ET.Element("V")
            child.text = str(self.v)
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueList":
        """Deserialize XML element to ValueList object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ValueList, cls).deserialize(element)

        # Parse v
        child = SerializationHelper.find_child_element(element, "V")
        if child is not None:
            v_value = SerializationHelper.deserialize_by_tag(child, "Numerical")
            obj.v = v_value

        return obj



class ValueListBuilder(BuilderBase):
    """Builder for ValueList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ValueList = ValueList()


    def with_v(self, value: Optional[Numerical]) -> "ValueListBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'v' is required and cannot be None")
        self._obj.v = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "v",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ValueList:
        """Build and return the ValueList instance with validation."""
        self._validate_instance()
        return self._obj