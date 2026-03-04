"""EndToEndProtection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EndToEndProtection(Identifiable):
    """AUTOSAR EndToEndProtection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "END-TO-END-PROTECTION"


    end_to_ends: list[EndToEndProtection]
    _DESERIALIZE_DISPATCH = {
        "END-TO-ENDS": lambda obj, elem: obj.end_to_ends.append(SerializationHelper.deserialize_by_tag(elem, "EndToEndProtection")),
    }


    def __init__(self) -> None:
        """Initialize EndToEndProtection."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []

    def serialize(self) -> ET.Element:
        """Serialize EndToEndProtection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndProtection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize end_to_ends (list to container "END-TO-ENDS")
        if self.end_to_ends:
            wrapper = ET.Element("END-TO-ENDS")
            for item in self.end_to_ends:
                serialized = SerializationHelper.serialize_item(item, "EndToEndProtection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtection":
        """Deserialize XML element to EndToEndProtection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "END-TO-ENDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.end_to_ends.append(SerializationHelper.deserialize_by_tag(item_elem, "EndToEndProtection"))

        return obj



class EndToEndProtectionBuilder(IdentifiableBuilder):
    """Builder for EndToEndProtection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndProtection = EndToEndProtection()


    def with_end_to_ends(self, items: list[EndToEndProtection]) -> "EndToEndProtectionBuilder":
        """Set end_to_ends list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.end_to_ends = list(items) if items else []
        return self


    def add_end_to_end(self, item: EndToEndProtection) -> "EndToEndProtectionBuilder":
        """Add a single item to end_to_ends list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.end_to_ends.append(item)
        return self

    def clear_end_to_ends(self) -> "EndToEndProtectionBuilder":
        """Clear all items from end_to_ends list.

        Returns:
            self for method chaining
        """
        self._obj.end_to_ends = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "endToEnd",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EndToEndProtection:
        """Build and return the EndToEndProtection instance with validation."""
        self._validate_instance()
        return self._obj