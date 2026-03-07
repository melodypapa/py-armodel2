"""CommunicationBufferLocking AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import SwcSupportedFeatureBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    SupportBufferLockingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommunicationBufferLocking(SwcSupportedFeature):
    """AUTOSAR CommunicationBufferLocking."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMMUNICATION-BUFFER-LOCKING"


    support_buffer_locking: Optional[SupportBufferLockingEnum]
    _DESERIALIZE_DISPATCH = {
        "SUPPORT-BUFFER-LOCKING": lambda obj, elem: setattr(obj, "support_buffer_locking", SupportBufferLockingEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CommunicationBufferLocking."""
        super().__init__()
        self.support_buffer_locking: Optional[SupportBufferLockingEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationBufferLocking to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationBufferLocking, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize support_buffer_locking
        if self.support_buffer_locking is not None:
            serialized = SerializationHelper.serialize_item(self.support_buffer_locking, "SupportBufferLockingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-BUFFER-LOCKING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationBufferLocking":
        """Deserialize XML element to CommunicationBufferLocking object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationBufferLocking object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationBufferLocking, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SUPPORT-BUFFER-LOCKING":
                setattr(obj, "support_buffer_locking", SupportBufferLockingEnum.deserialize(child))

        return obj



class CommunicationBufferLockingBuilder(SwcSupportedFeatureBuilder):
    """Builder for CommunicationBufferLocking with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationBufferLocking = CommunicationBufferLocking()


    def with_support_buffer_locking(self, value: Optional[SupportBufferLockingEnum]) -> "CommunicationBufferLockingBuilder":
        """Set support_buffer_locking attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'support_buffer_locking' is required and cannot be None")
        self._obj.support_buffer_locking = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "supportBufferLocking",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CommunicationBufferLocking:
        """Build and return the CommunicationBufferLocking instance with validation."""
        self._validate_instance()
        return self._obj