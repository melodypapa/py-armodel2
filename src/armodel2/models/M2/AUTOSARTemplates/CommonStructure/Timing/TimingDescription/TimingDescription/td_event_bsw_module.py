"""TDEventBswModule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import TDEventBswBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-BSW-MODULE"


    bsw_module_entry_entry_ref: Optional[ARRef]
    td_event_bsw: Optional[TDEventBswModule]
    _DESERIALIZE_DISPATCH = {
        "BSW-MODULE-ENTRY-ENTRY-REF": lambda obj, elem: setattr(obj, "bsw_module_entry_entry_ref", ARRef.deserialize(elem)),
        "TD-EVENT-BSW": lambda obj, elem: setattr(obj, "td_event_bsw", SerializationHelper.deserialize_by_tag(elem, "TDEventBswModule")),
    }


    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry_ref: Optional[ARRef] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBswModule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswModule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_entry_entry_ref
        if self.bsw_module_entry_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_entry_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTRY-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_bsw
        if self.td_event_bsw is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_bsw, "TDEventBswModule")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModule":
        """Deserialize XML element to TDEventBswModule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswModule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswModule, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-MODULE-ENTRY-ENTRY-REF":
                setattr(obj, "bsw_module_entry_entry_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-BSW":
                setattr(obj, "td_event_bsw", SerializationHelper.deserialize_by_tag(child, "TDEventBswModule"))

        return obj



class TDEventBswModuleBuilder(TDEventBswBuilder):
    """Builder for TDEventBswModule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventBswModule = TDEventBswModule()


    def with_bsw_module_entry_entry(self, value: Optional[BswModuleEntry]) -> "TDEventBswModuleBuilder":
        """Set bsw_module_entry_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_module_entry_entry = value
        return self

    def with_td_event_bsw(self, value: Optional[TDEventBswModule]) -> "TDEventBswModuleBuilder":
        """Set td_event_bsw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_bsw = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswModuleEntryEntry",
        "tdEventBsw",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventBswModule:
        """Build and return the TDEventBswModule instance with validation."""
        self._validate_instance()
        return self._obj