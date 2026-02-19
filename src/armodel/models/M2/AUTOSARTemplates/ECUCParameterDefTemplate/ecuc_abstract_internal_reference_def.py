"""EcucAbstractInternalReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
    EcucAbstractReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """AUTOSAR EcucAbstractInternalReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    requires: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractInternalReferenceDef."""
        super().__init__()
        self.requires: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractInternalReferenceDef":
        """Deserialize XML element to EcucAbstractInternalReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractInternalReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractInternalReferenceDef, cls).deserialize(element)

        # Parse requires
        child = ARObject._find_child_element(element, "REQUIRES")
        if child is not None:
            requires_value = child.text
            obj.requires = requires_value

        return obj



class EcucAbstractInternalReferenceDefBuilder:
    """Builder for EcucAbstractInternalReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractInternalReferenceDef = EcucAbstractInternalReferenceDef()

    def build(self) -> EcucAbstractInternalReferenceDef:
        """Build and return EcucAbstractInternalReferenceDef object.

        Returns:
            EcucAbstractInternalReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
