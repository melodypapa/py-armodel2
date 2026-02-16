"""InternalConstrs AUTOSAR element."""

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


class InternalConstrs(ARObject):
    """AUTOSAR InternalConstrs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_limit", None, True, False, None),  # lowerLimit
        ("max_diff", None, True, False, None),  # maxDiff
        ("max_gradient", None, True, False, None),  # maxGradient
        ("monotony", None, False, False, MonotonyEnum),  # monotony
        ("scale_constrs", None, False, True, ScaleConstr),  # scaleConstrs
        ("upper_limit", None, True, False, None),  # upperLimit
    ]

    def __init__(self) -> None:
        """Initialize InternalConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.upper_limit: Optional[Limit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InternalConstrs to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalConstrs":
        """Create InternalConstrs from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InternalConstrs instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InternalConstrs since parent returns ARObject
        return cast("InternalConstrs", obj)


class InternalConstrsBuilder:
    """Builder for InternalConstrs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalConstrs = InternalConstrs()

    def build(self) -> InternalConstrs:
        """Build and return InternalConstrs object.

        Returns:
            InternalConstrs instance
        """
        # TODO: Add validation
        return self._obj
