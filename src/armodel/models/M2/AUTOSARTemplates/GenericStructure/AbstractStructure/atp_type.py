"""AtpType AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AtpType(Identifiable, ABC):
    """AUTOSAR AtpType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AtpType."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpType":
        """Deserialize XML element to AtpType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpType object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AtpType, cls).deserialize(element)



class AtpTypeBuilder:
    """Builder for AtpType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpType = AtpType()

    def build(self) -> AtpType:
        """Build and return AtpType object.

        Returns:
            AtpType instance
        """
        # TODO: Add validation
        return self._obj
