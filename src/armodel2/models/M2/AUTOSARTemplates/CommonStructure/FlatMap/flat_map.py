"""FlatMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 965)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 445)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlatMap(ARElement):
    """AUTOSAR FlatMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLAT-MAP"


    instances: list[FlatInstanceDescriptor]
    _DESERIALIZE_DISPATCH = {
        "INSTANCES": lambda obj, elem: obj.instances.append(SerializationHelper.deserialize_by_tag(elem, "FlatInstanceDescriptor")),
    }


    def __init__(self) -> None:
        """Initialize FlatMap."""
        super().__init__()
        self.instances: list[FlatInstanceDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize FlatMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlatMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize instances (list to container "INSTANCES")
        if self.instances:
            wrapper = ET.Element("INSTANCES")
            for item in self.instances:
                serialized = SerializationHelper.serialize_item(item, "FlatInstanceDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatMap":
        """Deserialize XML element to FlatMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlatMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlatMap, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INSTANCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.instances.append(SerializationHelper.deserialize_by_tag(item_elem, "FlatInstanceDescriptor"))

        return obj



class FlatMapBuilder(ARElementBuilder):
    """Builder for FlatMap with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlatMap = FlatMap()


    def with_instances(self, items: list[FlatInstanceDescriptor]) -> "FlatMapBuilder":
        """Set instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instances = list(items) if items else []
        return self


    def add_instance(self, item: FlatInstanceDescriptor) -> "FlatMapBuilder":
        """Add a single item to instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instances.append(item)
        return self

    def clear_instances(self) -> "FlatMapBuilder":
        """Clear all items from instances list.

        Returns:
            self for method chaining
        """
        self._obj.instances = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "instance",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlatMap:
        """Build and return the FlatMap instance with validation."""
        self._validate_instance()
        return self._obj