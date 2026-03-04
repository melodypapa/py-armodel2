"""UserDefinedGlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 879)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_UserDefined.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import GlobalTimeMasterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    """AUTOSAR UserDefinedGlobalTimeMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "USER-DEFINED-GLOBAL-TIME-MASTER"


    def __init__(self) -> None:
        """Initialize UserDefinedGlobalTimeMaster."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize UserDefinedGlobalTimeMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedGlobalTimeMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedGlobalTimeMaster":
        """Deserialize XML element to UserDefinedGlobalTimeMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedGlobalTimeMaster object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedGlobalTimeMaster, cls).deserialize(element)



class UserDefinedGlobalTimeMasterBuilder(GlobalTimeMasterBuilder):
    """Builder for UserDefinedGlobalTimeMaster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UserDefinedGlobalTimeMaster = UserDefinedGlobalTimeMaster()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UserDefinedGlobalTimeMaster:
        """Build and return the UserDefinedGlobalTimeMaster instance with validation."""
        self._validate_instance()
        return self._obj