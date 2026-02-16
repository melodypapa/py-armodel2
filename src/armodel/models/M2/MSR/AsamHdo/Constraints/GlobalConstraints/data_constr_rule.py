"""DataConstrRule AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import (
    InternalConstrs,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.phys_constrs import (
    PhysConstrs,
)


class DataConstrRule(ARObject):
    """AUTOSAR DataConstrRule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("constr_level", None, True, False, None),  # constrLevel
        ("internal_constrs", None, False, False, InternalConstrs),  # internalConstrs
        ("phys_constrs", None, False, False, PhysConstrs),  # physConstrs
    ]

    def __init__(self) -> None:
        """Initialize DataConstrRule."""
        super().__init__()
        self.constr_level: Optional[Integer] = None
        self.internal_constrs: Optional[InternalConstrs] = None
        self.phys_constrs: Optional[PhysConstrs] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataConstrRule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstrRule":
        """Create DataConstrRule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataConstrRule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataConstrRule since parent returns ARObject
        return cast("DataConstrRule", obj)


class DataConstrRuleBuilder:
    """Builder for DataConstrRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstrRule = DataConstrRule()

    def build(self) -> DataConstrRule:
        """Build and return DataConstrRule object.

        Returns:
            DataConstrRule instance
        """
        # TODO: Add validation
        return self._obj
