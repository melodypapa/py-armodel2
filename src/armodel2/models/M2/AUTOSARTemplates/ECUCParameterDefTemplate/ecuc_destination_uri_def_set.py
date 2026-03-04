"""EcucDestinationUriDefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDestinationUriDefSet(ARElement):
    """AUTOSAR EcucDestinationUriDefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-DESTINATION-URI-DEF-SET"


    destination_uri_defs: list[EcucDestinationUriDef]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-URI-DEFS": lambda obj, elem: obj.destination_uri_defs.append(SerializationHelper.deserialize_by_tag(elem, "EcucDestinationUriDef")),
    }


    def __init__(self) -> None:
        """Initialize EcucDestinationUriDefSet."""
        super().__init__()
        self.destination_uri_defs: list[EcucDestinationUriDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriDefSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriDefSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri_defs (list to container "DESTINATION-URI-DEFS")
        if self.destination_uri_defs:
            wrapper = ET.Element("DESTINATION-URI-DEFS")
            for item in self.destination_uri_defs:
                serialized = SerializationHelper.serialize_item(item, "EcucDestinationUriDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDefSet":
        """Deserialize XML element to EcucDestinationUriDefSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDefSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriDefSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-URI-DEFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.destination_uri_defs.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucDestinationUriDef"))

        return obj



class EcucDestinationUriDefSetBuilder(ARElementBuilder):
    """Builder for EcucDestinationUriDefSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDestinationUriDefSet = EcucDestinationUriDefSet()


    def with_destination_uri_defs(self, items: list[EcucDestinationUriDef]) -> "EcucDestinationUriDefSetBuilder":
        """Set destination_uri_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.destination_uri_defs = list(items) if items else []
        return self


    def add_destination_uri_def(self, item: EcucDestinationUriDef) -> "EcucDestinationUriDefSetBuilder":
        """Add a single item to destination_uri_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.destination_uri_defs.append(item)
        return self

    def clear_destination_uri_defs(self) -> "EcucDestinationUriDefSetBuilder":
        """Clear all items from destination_uri_defs list.

        Returns:
            self for method chaining
        """
        self._obj.destination_uri_defs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "destinationUriDef",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucDestinationUriDefSet:
        """Build and return the EcucDestinationUriDefSet instance with validation."""
        self._validate_instance()
        return self._obj