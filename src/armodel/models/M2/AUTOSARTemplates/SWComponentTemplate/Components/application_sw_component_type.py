"""ApplicationSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 71)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1998)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 205)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationSwComponentType(AtomicSwComponentType):
    """AUTOSAR ApplicationSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ApplicationSwComponentType."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationSwComponentType":
        """Deserialize XML element to ApplicationSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class ApplicationSwComponentTypeBuilder:
    """Builder for ApplicationSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationSwComponentType = ApplicationSwComponentType()

    def build(self) -> ApplicationSwComponentType:
        """Build and return ApplicationSwComponentType object.

        Returns:
            ApplicationSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
