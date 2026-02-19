"""AtpPrototype AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
    AtpType,
)
from abc import ABC, abstractmethod


class AtpPrototype(Identifiable, ABC):
    """AUTOSAR AtpPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_type: AtpType
    def __init__(self) -> None:
        """Initialize AtpPrototype."""
        super().__init__()
        self.atp_type: AtpType = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpPrototype":
        """Deserialize XML element to AtpPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpPrototype, cls).deserialize(element)

        # Parse atp_type
        child = ARObject._find_child_element(element, "ATP-TYPE")
        if child is not None:
            atp_type_value = ARObject._deserialize_by_tag(child, "AtpType")
            obj.atp_type = atp_type_value

        return obj



class AtpPrototypeBuilder:
    """Builder for AtpPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpPrototype = AtpPrototype()

    def build(self) -> AtpPrototype:
        """Build and return AtpPrototype object.

        Returns:
            AtpPrototype instance
        """
        # TODO: Add validation
        return self._obj
