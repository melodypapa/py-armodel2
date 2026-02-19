"""SaveConfigurationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SaveConfigurationEntry(LinConfigurationEntry):
    """AUTOSAR SaveConfigurationEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SaveConfigurationEntry."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SaveConfigurationEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SaveConfigurationEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SaveConfigurationEntry":
        """Deserialize XML element to SaveConfigurationEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SaveConfigurationEntry object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SaveConfigurationEntry, cls).deserialize(element)



class SaveConfigurationEntryBuilder:
    """Builder for SaveConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SaveConfigurationEntry = SaveConfigurationEntry()

    def build(self) -> SaveConfigurationEntry:
        """Build and return SaveConfigurationEntry object.

        Returns:
            SaveConfigurationEntry instance
        """
        # TODO: Add validation
        return self._obj
