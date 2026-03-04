"""UserDefinedEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 579)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import AbstractEthernetFrameBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UserDefinedEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR UserDefinedEthernetFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "USER-DEFINED-ETHERNET-FRAME"


    def __init__(self) -> None:
        """Initialize UserDefinedEthernetFrame."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize UserDefinedEthernetFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedEthernetFrame, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "UserDefinedEthernetFrame":
        """Deserialize XML element to UserDefinedEthernetFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedEthernetFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedEthernetFrame, cls).deserialize(element)



class UserDefinedEthernetFrameBuilder(AbstractEthernetFrameBuilder):
    """Builder for UserDefinedEthernetFrame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UserDefinedEthernetFrame = UserDefinedEthernetFrame()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UserDefinedEthernetFrame:
        """Build and return the UserDefinedEthernetFrame instance with validation."""
        self._validate_instance()
        return self._obj