"""EndToEndTransformationComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2023)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_from_valid: Optional[Boolean]
    disable_end_to: Optional[Boolean]
    e2e_profile: Optional[E2EProfileCompatibilityProps]
    max_delta: Optional[PositiveInteger]
    max_error_state: Optional[PositiveInteger]
    max_no_new_or: Optional[PositiveInteger]
    min_ok_state_init: Optional[PositiveInteger]
    min_ok_state: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    window_size_init: Optional[PositiveInteger]
    window_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None


class EndToEndTransformationComSpecPropsBuilder:
    """Builder for EndToEndTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()

    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return EndToEndTransformationComSpecProps object.

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
