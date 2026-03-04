"""TtcanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import AbstractCanCommunicationConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TtcanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR TtcanCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TTCAN-COMMUNICATION-CONNECTOR"


    def __init__(self) -> None:
        """Initialize TtcanCommunicationConnector."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize TtcanCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TtcanCommunicationConnector, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "TtcanCommunicationConnector":
        """Deserialize XML element to TtcanCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCommunicationConnector object
        """
        # Delegate to parent class to handle inherited attributes
        return super(TtcanCommunicationConnector, cls).deserialize(element)



class TtcanCommunicationConnectorBuilder(AbstractCanCommunicationConnectorBuilder):
    """Builder for TtcanCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TtcanCommunicationConnector = TtcanCommunicationConnector()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TtcanCommunicationConnector:
        """Build and return the TtcanCommunicationConnector instance with validation."""
        self._validate_instance()
        return self._obj