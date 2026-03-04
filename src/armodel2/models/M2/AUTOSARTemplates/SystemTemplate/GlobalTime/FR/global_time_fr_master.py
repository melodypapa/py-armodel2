"""GlobalTimeFrMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 877)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import GlobalTimeMasterBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeCrcSupportEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeFrMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeFrMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-FR-MASTER"


    crc_secured: Optional[GlobalTimeCrcSupportEnum]
    _DESERIALIZE_DISPATCH = {
        "CRC-SECURED": lambda obj, elem: setattr(obj, "crc_secured", GlobalTimeCrcSupportEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeFrMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeFrMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeFrMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_secured
        if self.crc_secured is not None:
            serialized = SerializationHelper.serialize_item(self.crc_secured, "GlobalTimeCrcSupportEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SECURED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeFrMaster":
        """Deserialize XML element to GlobalTimeFrMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeFrMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeFrMaster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CRC-SECURED":
                setattr(obj, "crc_secured", GlobalTimeCrcSupportEnum.deserialize(child))

        return obj



class GlobalTimeFrMasterBuilder(GlobalTimeMasterBuilder):
    """Builder for GlobalTimeFrMaster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeFrMaster = GlobalTimeFrMaster()


    def with_crc_secured(self, value: Optional[GlobalTimeCrcSupportEnum]) -> "GlobalTimeFrMasterBuilder":
        """Set crc_secured attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_secured = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "crcSecured",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GlobalTimeFrMaster:
        """Build and return the GlobalTimeFrMaster instance with validation."""
        self._validate_instance()
        return self._obj