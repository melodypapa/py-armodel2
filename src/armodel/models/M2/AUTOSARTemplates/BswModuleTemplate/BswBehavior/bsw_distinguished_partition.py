"""BswDistinguishedPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswDistinguishedPartition(Referrable):
    """AUTOSAR BswDistinguishedPartition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswDistinguishedPartition."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDistinguishedPartition":
        """Deserialize XML element to BswDistinguishedPartition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswDistinguishedPartition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class BswDistinguishedPartitionBuilder:
    """Builder for BswDistinguishedPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDistinguishedPartition = BswDistinguishedPartition()

    def build(self) -> BswDistinguishedPartition:
        """Build and return BswDistinguishedPartition object.

        Returns:
            BswDistinguishedPartition instance
        """
        # TODO: Add validation
        return self._obj
