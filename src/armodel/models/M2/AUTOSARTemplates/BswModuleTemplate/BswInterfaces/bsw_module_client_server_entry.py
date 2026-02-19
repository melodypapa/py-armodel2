"""BswModuleClientServerEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    encapsulated: Optional[BswModuleEntry]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated: Optional[BswModuleEntry] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleClientServerEntry":
        """Deserialize XML element to BswModuleClientServerEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleClientServerEntry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse encapsulated
        child = ARObject._find_child_element(element, "ENCAPSULATED")
        if child is not None:
            encapsulated_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.encapsulated = encapsulated_value

        # Parse is_reentrant
        child = ARObject._find_child_element(element, "IS-REENTRANT")
        if child is not None:
            is_reentrant_value = child.text
            obj.is_reentrant = is_reentrant_value

        # Parse is_synchronous
        child = ARObject._find_child_element(element, "IS-SYNCHRONOUS")
        if child is not None:
            is_synchronous_value = child.text
            obj.is_synchronous = is_synchronous_value

        return obj



class BswModuleClientServerEntryBuilder:
    """Builder for BswModuleClientServerEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()

    def build(self) -> BswModuleClientServerEntry:
        """Build and return BswModuleClientServerEntry object.

        Returns:
            BswModuleClientServerEntry instance
        """
        # TODO: Add validation
        return self._obj
