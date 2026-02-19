"""EcucAbstractReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucAbstractReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceDef."""
        super().__init__()
        self.with_auto: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceDef":
        """Deserialize XML element to EcucAbstractReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractReferenceDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse with_auto
        child = ARObject._find_child_element(element, "WITH-AUTO")
        if child is not None:
            with_auto_value = child.text
            obj.with_auto = with_auto_value

        return obj



class EcucAbstractReferenceDefBuilder:
    """Builder for EcucAbstractReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceDef = EcucAbstractReferenceDef()

    def build(self) -> EcucAbstractReferenceDef:
        """Build and return EcucAbstractReferenceDef object.

        Returns:
            EcucAbstractReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
