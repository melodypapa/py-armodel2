"""SdgDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SdgDef(ARElement):
    """AUTOSAR SdgDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG-DEF"


    sdg_classes: list[SdgClass]
    _DESERIALIZE_DISPATCH = {
        "SDG-CLASSS": lambda obj, elem: obj.sdg_classes.append(SerializationHelper.deserialize_by_tag(elem, "SdgClass")),
    }


    def __init__(self) -> None:
        """Initialize SdgDef."""
        super().__init__()
        self.sdg_classes: list[SdgClass] = []

    def serialize(self) -> ET.Element:
        """Serialize SdgDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sdg_classes (list to container "SDG-CLASSS")
        if self.sdg_classes:
            wrapper = ET.Element("SDG-CLASSS")
            for item in self.sdg_classes:
                serialized = SerializationHelper.serialize_item(item, "SdgClass")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgDef":
        """Deserialize XML element to SdgDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SDG-CLASSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sdg_classes.append(SerializationHelper.deserialize_by_tag(item_elem, "SdgClass"))

        return obj



class SdgDefBuilder(ARElementBuilder):
    """Builder for SdgDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgDef = SdgDef()


    def with_sdg_classes(self, items: list[SdgClass]) -> "SdgDefBuilder":
        """Set sdg_classes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdg_classes = list(items) if items else []
        return self


    def add_sdg_class(self, item: SdgClass) -> "SdgDefBuilder":
        """Add a single item to sdg_classes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdg_classes.append(item)
        return self

    def clear_sdg_classes(self) -> "SdgDefBuilder":
        """Clear all items from sdg_classes list.

        Returns:
            self for method chaining
        """
        self._obj.sdg_classes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "sdgClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SdgDef:
        """Build and return the SdgDef instance with validation."""
        self._validate_instance()
        return self._obj