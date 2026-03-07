"""BswOperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import BswEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswOperationInvokedEvent(BswEvent):
    """AUTOSAR BswOperationInvokedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-OPERATION-INVOKED-EVENT"


    entry_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ENTRY-REF": lambda obj, elem: setattr(obj, "entry_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswOperationInvokedEvent."""
        super().__init__()
        self.entry_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswOperationInvokedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswOperationInvokedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entry_ref
        if self.entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.entry_ref, "BswModuleClientServerEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswOperationInvokedEvent":
        """Deserialize XML element to BswOperationInvokedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswOperationInvokedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswOperationInvokedEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENTRY-REF":
                setattr(obj, "entry_ref", ARRef.deserialize(child))

        return obj



class BswOperationInvokedEventBuilder(BswEventBuilder):
    """Builder for BswOperationInvokedEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswOperationInvokedEvent = BswOperationInvokedEvent()


    def with_entry(self, value: Optional[BswModuleClientServerEntry]) -> "BswOperationInvokedEventBuilder":
        """Set entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'entry' is required and cannot be None")
        self._obj.entry = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "entry",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswOperationInvokedEvent:
        """Build and return the BswOperationInvokedEvent instance with validation."""
        self._validate_instance()
        return self._obj