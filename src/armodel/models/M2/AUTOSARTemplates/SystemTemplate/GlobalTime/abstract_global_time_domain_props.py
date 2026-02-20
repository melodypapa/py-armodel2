"""AbstractGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractGlobalTimeDomainProps(ARObject, ABC):
    """AUTOSAR AbstractGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractGlobalTimeDomainProps."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AbstractGlobalTimeDomainProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractGlobalTimeDomainProps":
        """Deserialize XML element to AbstractGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractGlobalTimeDomainProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class AbstractGlobalTimeDomainPropsBuilder:
    """Builder for AbstractGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractGlobalTimeDomainProps = AbstractGlobalTimeDomainProps()

    def build(self) -> AbstractGlobalTimeDomainProps:
        """Build and return AbstractGlobalTimeDomainProps object.

        Returns:
            AbstractGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
