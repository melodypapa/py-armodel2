"""InvalidationPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InvalidationPolicy(ARObject):
    """AUTOSAR InvalidationPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # dataElement
        "handle_invalid_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HandleInvalidEnum,
        ),  # handleInvalidEnum
    }

    def __init__(self) -> None:
        """Initialize InvalidationPolicy."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None


class InvalidationPolicyBuilder:
    """Builder for InvalidationPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvalidationPolicy = InvalidationPolicy()

    def build(self) -> InvalidationPolicy:
        """Build and return InvalidationPolicy object.

        Returns:
            InvalidationPolicy instance
        """
        # TODO: Add validation
        return self._obj
