"""PhysConstrs AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lower_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # lowerLimit
        "max_diff": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDiff
        "max_gradient": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxGradient
        "monotony": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MonotonyEnum,
        ),  # monotony
        "scale_constrs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ScaleConstr,
        ),  # scaleConstrs
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
        "upper_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperLimit
    }

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
