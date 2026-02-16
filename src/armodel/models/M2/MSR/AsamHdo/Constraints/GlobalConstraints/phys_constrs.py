"""PhysConstrs AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
    ScaleConstr,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class PhysConstrs(ARObject):
    """AUTOSAR PhysConstrs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_limit", None, True, False, None),  # lowerLimit
        ("max_diff", None, True, False, None),  # maxDiff
        ("max_gradient", None, True, False, None),  # maxGradient
        ("monotony", None, False, False, MonotonyEnum),  # monotony
        ("scale_constrs", None, False, True, ScaleConstr),  # scaleConstrs
        ("unit", None, False, False, Unit),  # unit
        ("upper_limit", None, True, False, None),  # upperLimit
    ]

    def __init__(self) -> None:
        """Initialize PhysConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.unit: Optional[Unit] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PhysConstrs to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysConstrs":
        """Create PhysConstrs from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PhysConstrs instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PhysConstrs since parent returns ARObject
        return cast("PhysConstrs", obj)


class PhysConstrsBuilder:
    """Builder for PhysConstrs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysConstrs = PhysConstrs()

    def build(self) -> PhysConstrs:
        """Build and return PhysConstrs object.

        Returns:
            PhysConstrs instance
        """
        # TODO: Add validation
        return self._obj
