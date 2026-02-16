"""SwGenericAxisParamType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)


class SwGenericAxisParamType(Identifiable):
    """AUTOSAR SwGenericAxisParamType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_constr": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataConstr,
        ),  # dataConstr
    }

    def __init__(self) -> None:
        """Initialize SwGenericAxisParamType."""
        super().__init__()
        self.data_constr: Optional[DataConstr] = None


class SwGenericAxisParamTypeBuilder:
    """Builder for SwGenericAxisParamType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParamType = SwGenericAxisParamType()

    def build(self) -> SwGenericAxisParamType:
        """Build and return SwGenericAxisParamType object.

        Returns:
            SwGenericAxisParamType instance
        """
        # TODO: Add validation
        return self._obj
