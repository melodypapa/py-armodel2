"""CommunicationCycle AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class CommunicationCycle(ARObject, ABC):
    """AUTOSAR CommunicationCycle."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CommunicationCycle."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize CommunicationCycle to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationCycle":
        """Deserialize XML element to CommunicationCycle object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationCycle object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class CommunicationCycleBuilder:
    """Builder for CommunicationCycle."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationCycle = CommunicationCycle()

    def build(self) -> CommunicationCycle:
        """Build and return CommunicationCycle object.

        Returns:
            CommunicationCycle instance
        """
        # TODO: Add validation
        return self._obj
