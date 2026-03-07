"""DltEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_application import (
    DltApplication,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltEcu(ARElement):
    """AUTOSAR DltEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-ECU"


    applications: list[DltApplication]
    ecu_id: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "APPLICATIONS": lambda obj, elem: obj.applications.append(SerializationHelper.deserialize_by_tag(elem, "DltApplication")),
        "ECU-ID": lambda obj, elem: setattr(obj, "ecu_id", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize DltEcu."""
        super().__init__()
        self.applications: list[DltApplication] = []
        self.ecu_id: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DltEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = SerializationHelper.serialize_item(item, "DltApplication")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_id
        if self.ecu_id is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltEcu":
        """Deserialize XML element to DltEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltEcu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.applications.append(SerializationHelper.deserialize_by_tag(item_elem, "DltApplication"))
            elif tag == "ECU-ID":
                setattr(obj, "ecu_id", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class DltEcuBuilder(ARElementBuilder):
    """Builder for DltEcu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltEcu = DltEcu()


    def with_applications(self, items: list[DltApplication]) -> "DltEcuBuilder":
        """Set applications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applications = list(items) if items else []
        return self

    def with_ecu_id(self, value: Optional[String]) -> "DltEcuBuilder":
        """Set ecu_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ecu_id' is required and cannot be None")
        self._obj.ecu_id = value
        return self


    def add_application(self, item: DltApplication) -> "DltEcuBuilder":
        """Add a single item to applications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applications.append(item)
        return self

    def clear_applications(self) -> "DltEcuBuilder":
        """Clear all items from applications list.

        Returns:
            self for method chaining
        """
        self._obj.applications = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "application",
        "ecuId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DltEcu:
        """Build and return the DltEcu instance with validation."""
        self._validate_instance()
        return self._obj