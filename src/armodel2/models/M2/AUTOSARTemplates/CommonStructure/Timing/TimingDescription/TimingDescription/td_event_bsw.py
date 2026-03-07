"""TDEventBsw AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 251)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import TimingDescriptionEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventBsw(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventBsw."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bsw_module_description_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BSW-MODULE-DESCRIPTION-REF": lambda obj, elem: setattr(obj, "bsw_module_description_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventBsw."""
        super().__init__()
        self.bsw_module_description_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBsw to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBsw, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_description_ref
        if self.bsw_module_description_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_description_ref, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-DESCRIPTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBsw":
        """Deserialize XML element to TDEventBsw object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBsw object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBsw, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-MODULE-DESCRIPTION-REF":
                setattr(obj, "bsw_module_description_ref", ARRef.deserialize(child))

        return obj



class TDEventBswBuilder(TimingDescriptionEventBuilder):
    """Builder for TDEventBsw with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventBsw = TDEventBsw()


    def with_bsw_module_description(self, value: Optional[BswModuleDescription]) -> "TDEventBswBuilder":
        """Set bsw_module_description attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'bsw_module_description' is required and cannot be None")
        self._obj.bsw_module_description = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswModuleDescription",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> TDEventBsw:
        """Build and return the TDEventBsw instance (abstract)."""
        raise NotImplementedError