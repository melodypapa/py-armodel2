"""BswVariableAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswVariableAccess(Referrable):
    """AUTOSAR BswVariableAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accessed_variable", None, False, False, VariableDataPrototype),  # accessedVariable
        ("contexts", None, False, True, BswDistinguishedPartition),  # contexts
    ]

    def __init__(self) -> None:
        """Initialize BswVariableAccess."""
        super().__init__()
        self.accessed_variable: Optional[VariableDataPrototype] = None
        self.contexts: list[BswDistinguishedPartition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswVariableAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswVariableAccess":
        """Create BswVariableAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswVariableAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswVariableAccess since parent returns ARObject
        return cast("BswVariableAccess", obj)


class BswVariableAccessBuilder:
    """Builder for BswVariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswVariableAccess = BswVariableAccess()

    def build(self) -> BswVariableAccess:
        """Build and return BswVariableAccess object.

        Returns:
            BswVariableAccess instance
        """
        # TODO: Add validation
        return self._obj
