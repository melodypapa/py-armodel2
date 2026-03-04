"""GlobalTimeCouplingPortProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 875)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeCouplingPortProps(ARObject):
    """AUTOSAR GlobalTimeCouplingPortProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-COUPLING-PORT-PROPS"


    propagation: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "PROPAGATION": lambda obj, elem: setattr(obj, "propagation", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeCouplingPortProps."""
        super().__init__()
        self.propagation: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCouplingPortProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCouplingPortProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize propagation
        if self.propagation is not None:
            serialized = SerializationHelper.serialize_item(self.propagation, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROPAGATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCouplingPortProps":
        """Deserialize XML element to GlobalTimeCouplingPortProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCouplingPortProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCouplingPortProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROPAGATION":
                setattr(obj, "propagation", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class GlobalTimeCouplingPortPropsBuilder(BuilderBase):
    """Builder for GlobalTimeCouplingPortProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeCouplingPortProps = GlobalTimeCouplingPortProps()


    def with_propagation(self, value: Optional[TimeValue]) -> "GlobalTimeCouplingPortPropsBuilder":
        """Set propagation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.propagation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "propagation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GlobalTimeCouplingPortProps:
        """Build and return the GlobalTimeCouplingPortProps instance with validation."""
        self._validate_instance()
        return self._obj