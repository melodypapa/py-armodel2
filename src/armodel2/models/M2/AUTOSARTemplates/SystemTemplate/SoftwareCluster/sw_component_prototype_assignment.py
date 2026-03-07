"""SwComponentPrototypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 894)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwComponentPrototypeAssignment(ARObject):
    """AUTOSAR SwComponentPrototypeAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-COMPONENT-PROTOTYPE-ASSIGNMENT"


    sw_component: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "SW-COMPONENT": lambda obj, elem: setattr(obj, "sw_component", SerializationHelper.deserialize_by_tag(elem, "any (SwComponent)")),
    }


    def __init__(self) -> None:
        """Initialize SwComponentPrototypeAssignment."""
        super().__init__()
        self.sw_component: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentPrototypeAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentPrototypeAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_component
        if self.sw_component is not None:
            serialized = SerializationHelper.serialize_item(self.sw_component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototypeAssignment":
        """Deserialize XML element to SwComponentPrototypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototypeAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentPrototypeAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-COMPONENT":
                setattr(obj, "sw_component", SerializationHelper.deserialize_by_tag(child, "any (SwComponent)"))

        return obj



class SwComponentPrototypeAssignmentBuilder(BuilderBase):
    """Builder for SwComponentPrototypeAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwComponentPrototypeAssignment = SwComponentPrototypeAssignment()


    def with_sw_component(self, value: Optional[Any]) -> "SwComponentPrototypeAssignmentBuilder":
        """Set sw_component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_component' is required and cannot be None")
        self._obj.sw_component = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swComponent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwComponentPrototypeAssignment:
        """Build and return the SwComponentPrototypeAssignment instance with validation."""
        self._validate_instance()
        return self._obj