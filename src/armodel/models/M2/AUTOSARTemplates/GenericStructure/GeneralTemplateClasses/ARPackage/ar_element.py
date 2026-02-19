"""ARElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 297)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 286)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 58)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 967)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1992)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 71)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 54)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 55)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class ARElement(PackageableElement, ABC):
    """AUTOSAR ARElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize ARElement."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARElement":
        """Deserialize XML element to ARElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class ARElementBuilder:
    """Builder for ARElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARElement = ARElement()

    def build(self) -> ARElement:
        """Build and return ARElement object.

        Returns:
            ARElement instance
        """
        # TODO: Add validation
        return self._obj
