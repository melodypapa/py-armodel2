"""InvalidationPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InvalidationPolicy(ARObject):
    """AUTOSAR InvalidationPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element: Optional[VariableDataPrototype]
    handle_invalid_enum: Optional[HandleInvalidEnum]
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
