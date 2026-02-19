"""EcuPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcuPartition(Identifiable):
    """AUTOSAR EcuPartition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    exec_in_user: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcuPartition."""
        super().__init__()
        self.exec_in_user: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuPartition":
        """Deserialize XML element to EcuPartition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuPartition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuPartition, cls).deserialize(element)

        # Parse exec_in_user
        child = ARObject._find_child_element(element, "EXEC-IN-USER")
        if child is not None:
            exec_in_user_value = child.text
            obj.exec_in_user = exec_in_user_value

        return obj



class EcuPartitionBuilder:
    """Builder for EcuPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuPartition = EcuPartition()

    def build(self) -> EcuPartition:
        """Build and return EcuPartition object.

        Returns:
            EcuPartition instance
        """
        # TODO: Add validation
        return self._obj
