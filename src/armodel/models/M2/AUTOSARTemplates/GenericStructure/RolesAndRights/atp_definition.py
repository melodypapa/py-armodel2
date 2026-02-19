"""AtpDefinition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 383)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AtpDefinition(Referrable, ABC):
    """AUTOSAR AtpDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AtpDefinition."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpDefinition":
        """Deserialize XML element to AtpDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpDefinition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class AtpDefinitionBuilder:
    """Builder for AtpDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpDefinition = AtpDefinition()

    def build(self) -> AtpDefinition:
        """Build and return AtpDefinition object.

        Returns:
            AtpDefinition instance
        """
        # TODO: Add validation
        return self._obj
