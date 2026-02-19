"""PackageableElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 54)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class PackageableElement(CollectableElement, ABC):
    """AUTOSAR PackageableElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize PackageableElement."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PackageableElement":
        """Deserialize XML element to PackageableElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PackageableElement object
        """
        # Delegate to parent class to handle inherited attributes
        return super(PackageableElement, cls).deserialize(element)



class PackageableElementBuilder:
    """Builder for PackageableElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PackageableElement = PackageableElement()

    def build(self) -> PackageableElement:
        """Build and return PackageableElement object.

        Returns:
            PackageableElement instance
        """
        # TODO: Add validation
        return self._obj
