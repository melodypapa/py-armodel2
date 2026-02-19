"""DataInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DataInterface(PortInterface, ABC):
    """AUTOSAR DataInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DataInterface."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataInterface":
        """Deserialize XML element to DataInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataInterface object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DataInterface, cls).deserialize(element)



class DataInterfaceBuilder:
    """Builder for DataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataInterface = DataInterface()

    def build(self) -> DataInterface:
        """Build and return DataInterface object.

        Returns:
            DataInterface instance
        """
        # TODO: Add validation
        return self._obj
