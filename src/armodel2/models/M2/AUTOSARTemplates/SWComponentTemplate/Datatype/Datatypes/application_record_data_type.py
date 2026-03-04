"""ApplicationRecordDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import ApplicationCompositeDataTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_record_element import (
    ApplicationRecordElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationRecordDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-RECORD-DATA-TYPE"


    elements: list[ApplicationRecordElement]
    _DESERIALIZE_DISPATCH = {
        "ELEMENTS": lambda obj, elem: obj.elements.append(SerializationHelper.deserialize_by_tag(elem, "ApplicationRecordElement")),
    }


    def __init__(self) -> None:
        """Initialize ApplicationRecordDataType."""
        super().__init__()
        self.elements: list[ApplicationRecordElement] = []

    def serialize(self) -> ET.Element:
        """Serialize ApplicationRecordDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationRecordDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = SerializationHelper.serialize_item(item, "ApplicationRecordElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordDataType":
        """Deserialize XML element to ApplicationRecordDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRecordDataType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationRecordElement"))

        return obj



class ApplicationRecordDataTypeBuilder(ApplicationCompositeDataTypeBuilder):
    """Builder for ApplicationRecordDataType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationRecordDataType = ApplicationRecordDataType()


    def with_elements(self, items: list[ApplicationRecordElement]) -> "ApplicationRecordDataTypeBuilder":
        """Set elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elements = list(items) if items else []
        return self


    def add_element(self, item: ApplicationRecordElement) -> "ApplicationRecordDataTypeBuilder":
        """Add a single item to elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elements.append(item)
        return self

    def clear_elements(self) -> "ApplicationRecordDataTypeBuilder":
        """Clear all items from elements list.

        Returns:
            self for method chaining
        """
        self._obj.elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "element",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ApplicationRecordDataType:
        """Build and return the ApplicationRecordDataType instance with validation."""
        self._validate_instance()
        return self._obj